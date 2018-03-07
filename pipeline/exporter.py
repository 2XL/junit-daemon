import os, yaml


def str_presenter(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


yaml.add_representer(str, str_presenter)


class FixtureExporter(object):
    def __init__(self, source_home='src', test_home='tests', fixture_home='fixture', is_correct=False):
        self.source_home = source_home
        self.test_home = test_home
        self.fixture_home = fixture_home
        self.fixture = {}
        self.fixture_is_correct = is_correct
        if is_correct:
            self.fixture_case = 'initial'
        else:
            self.fixture_case = 'answer'
        pass

    def generate_fixture(self):
        self.fixture = {
            'challenge': {
                self.fixture_case: {
                    'is_correct': self.fixture_is_correct,
                    'files': []
                },
                'valid_assertion': {
                    'files': []
                }
            }
        }

        for source_file in self.collect_source_files():
            with open(source_file, 'r') as source_code:
                source = ['%%CREATE%%{source_path}%%\n'.format(source_path=source_file)]
                source = source + source_code.readlines()
                source.append('\n%%END')
                source_block = "".join(source)
                self.fixture['challenge'][self.fixture_case]['files'].append(source_block)
            pass
        for test_file in self.collect_valid_assertions():
            with open(test_file, 'r') as test_code:
                source = ['%%CREATE%%{source_path}%%\n'.format(source_path=test_file)]
                source = source + test_code.readlines()
                source.append('\n%%END')
                source_block = "".join(source)
                self.fixture['challenge']['valid_assertion']['files'].append(source_block)
            pass
        pass

    def collect_source_files(self):
        source_files = []
        for root, subdirs, files in os.walk(self.source_home):
            for file in files:
                if file.endswith('.java'):
                    source_files.append(os.path.join(root, file))
        return source_files

    def collect_valid_assertions(self):
        test_files = []
        for root, subdirs, files in os.walk(self.test_home):
            for file in files:
                if file.endswith('.java'):
                    test_files.append(os.path.join(root, file))

        return test_files
        pass

    def export_yml_fixture(self):
        with open(os.path.join(self.fixture_home, 'exported_challenge.yml'), 'w') as fixture_file:
            yaml.dump(self.fixture, fixture_file)
        pass


if __name__ == "__main__":
    os.chdir('..')
    exporter = FixtureExporter()
    exporter.generate_fixture()
    exporter.export_yml_fixture()
