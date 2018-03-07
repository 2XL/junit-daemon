import os, re, json


class ReportGenerator(object):
    def __init__(self, report_location='reports', report_extension_in='txt', report_extension_out='json'):
        self.report_location = report_location
        self.report_extension_in = report_extension_in
        self.report = None
        pass

    def generate_report(self):
        report_files = [pos_ for pos_ in os.listdir(self.report_location) if
                        pos_.endswith('.{}'.format(self.report_extension_in))]

        json_report = []
        for report in report_files:
            template = report.split('.')[0]
            parser = 'parse_{template}'.format(template=template)
            if hasattr(self, parser):
                json_report.append({template: getattr(self, parser)()})
                pass
        self.report = json_report

    def export_json_report(self):
        if self.report is None:
            pass
        else:
            with open(os.path.join(self.report_location, 'report.json'), 'w') as json_report:
                json_report.write(json.dumps(self.report, sort_keys=True, indent=2))  # , ensure_ascii=False

            pass

    def parse_err_compile_source(self):
        """
        Kayo
        ---------------------------------------------------------------------
        src/Person.java:1: error: '.' expected
        import magic
                     ^
        src/Person.java:3: error: ';' expected
        public class Person {
              ^
        src/Person.java:3: error: class, interface, or enum expected
        public class Person {
                     ^
        src/Person.java:6: error: class, interface, or enum expected
          public Person(String personName) {
                 ^
        src/Person.java:8: error: class, interface, or enum expected
          }
          ^
        src/Person.java:10: error: class, interface, or enum expected
          public String greet(String yourName) {
                 ^
        src/Person.java:13: error: class, interface, or enum expected
                  return String.format("Konbanwa!  My name is %s.  It is nice to meet you, %s!", this.name, yourName);
                  ^
        src/Person.java:14: error: class, interface, or enum expected
          }
          ^
        8 errors
        ---------------------------------------------------------------------

        :return:

        {
        "err_compile_source" : [
            {
            "line": "1"
            "column": "\^\^ length"
            "file": "src/Person.java",
            "message": "error: '.' expected",
            "source": "import obytes"
            },
            {
            etcetcetc
            }
        ]
        }

        """
        report_file = os.path.join(self.report_location, 'err_compile_source' + '.' + self.report_extension_in)

        err_compile_source = []

        masks = [
            r'^(?P<source_file>.*):(?P<source_line>.*):(?P<lint_type>.*):(?P<lint_message>.*)$',
            r'^(?P<source_code>.*)$',
            r'^(?P<source_position>.*)$'
        ]

        with open(report_file, 'r') as f:
            file_lines = f.readlines()
            offset = 3
            while len(file_lines) >= offset:  # while offset is lower than file_lines, continue
                line = file_lines[offset - 3:offset]

                match = re.match(masks[0], line[0])
                source_file = match.group('source_file')
                source_line = match.group('source_line')
                lint_type = match.group('lint_type')
                lint_message = match.group('lint_message')

                match = re.match(masks[1], line[1])
                source_code = match.group('source_code')

                match = re.match(masks[2], line[2])
                source_position = match.group('source_position')

                report_line = {
                    'source_file': source_file,
                    'source_line': source_line,
                    'lint_type': lint_type,
                    'lint_message': lint_message,
                    'source_code': source_code,
                    'source_column': len(source_position),
                }
                err_compile_source.append(report_line)
                offset = offset + 3

        return err_compile_source

        pass

    def parse_err_compile_test(self):
        """
        -------------------------------
        OKey
        -------------------------------

        -------------------------------
        Kayo
        -------------------------------

        -------------------------------

        :return:
        """
        # raise NotImplementedError
        return []
        pass

    def parse_err_run_test(self):
        """
        -------------------------------
        OKey
        -------------------------------

        -------------------------------
        Kayo
        -------------------------------

        -------------------------------

        :return:
        """
        # raise NotImplementedError
        # no demo source provided
        return []
        pass

    def parse_out_compile_source(self):
        """
        -------------------------------
        OKey
        -------------------------------

        -------------------------------
        Kayo
        -------------------------------

        -------------------------------

        :return:
        """
        # raise NotImplementedError
        return []
        pass

    def parse_out_compile_test(self):
        """
        -------------------------------
        OKey
        -------------------------------

        -------------------------------
        Kayo
        -------------------------------

        -------------------------------

        :return:
        """
        # raise NotImplementedError
        return []
        pass

    def parse_out_run_test(self):
        """
        -------------------------------
        OKey
        -------------------------------
        JUnit version 4.12
        .
        Time: 0.003

        OK (1 test)
        -------------------------------
        Kayo
        -------------------------------

        -------------------------------


        :return:
        {
        "out_run_test":
            {
            "framework-version": "JUnit version 4.12"
            "time": "0.003"
            "result": "OK"
            "summary": "(1 test)"
            }
        }
        """
        report_file = os.path.join(self.report_location, 'out_run_test' + '.' + self.report_extension_in)

        out_run_test = {}

        mask_result = r'^(?P<test_status>.*)\ \((?P<test_summary>.*)\).*$'

        with open(report_file, 'r') as f:
            lines = f.readlines()
            test_framework = lines[0].strip('\n')
            test_time = lines[2].rsplit(None, 1)[-1]

            match = re.match(mask_result, lines[4])
            test_status = match.group('test_status')
            test_summary = match.group('test_summary')

            out_run_test = {
                'test_framework': test_framework,
                'test_time': test_time,
                'test_status': test_status,
                'test_summary': test_summary
            }

            pass
        return out_run_test
        pass


if __name__ == "__main__":
    os.chdir('..')
    reporter = ReportGenerator()
    reporter.generate_report()
    reporter.export_json_report()
