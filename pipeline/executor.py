import os

class PipelineExecutor(object):

    def __init__(self):
        self.queue = []
        pass

    def load_queue_from_submission(self, code=''):
        """
        Initialize pipeline operations


        :return:
        :: generate java project tree with source from submission payload
        """
        file_source = None
        file_source_path = None
        file_jinja_key = None
        do_operation = None
        is_source = False
        for line in code.split('\n'):
            if line.startswith('%%'):
                split_line = line.split('%%')  # '%%CREATE%%app/models.py%%'
                operation = split_line[1]
                if operation != 'END':
                    do_operation = operation
                    is_source = True
                    file_source_path = split_line[2]
                    file_jinja_key = split_line[3]
                    file_source = []  # start empty file
                else:
                    is_source = False
                    self.queue.append({
                        'operation': do_operation,
                        'file_path': file_source_path,
                        'file_source': '\n'.join(file_source),
                        'jinja_key': file_jinja_key
                    })
            elif is_source:
                # append source
                file_source.append(line)

        pass

    def list_queue(self):
        for source_code in self.queue:
            print source_code['file_source']
        pass

    def apply_queue(self):
        for source_code in self.queue:
            to_apply = getattr(self, 'do_' + source_code['operation'].lower())
            assert to_apply(**source_code)
        pass

    def do_create(self, file_source, operation, file_path, jinja_key, *args, **kwargs):
        """
        # create or replace file with value
        %%CREATE%%file_path.file_name.extension%%
        value
        """

        directory = os.path.dirname(file_path)

        if not os.path.exists(directory):
            os.makedirs(directory)

        if os.path.isfile(file_path):
            pass  # just checking

        with open(file_path, 'w') as f:
            f.write(file_source)

        return True
        pass

    def do_update(self, *args, **kwargs):
        """
        # update source from existing file, lookup for a key
        %%UPDATE%%file_path.file_name.extension%%jinja.key%%
        value
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplemented
        return True
        pass

    def do_put(self, *args, **kwargs):
        """
        # append source to existing file or create new
        %%PUT%%file_path.file_name.extension%%
        value

        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplemented
        return True
        pass

    def do_drop(self, *args, **kwargs):
        """
        # drop file or secction of a file
        %%DROP%%file_path.file_name.extension%%key
        %%DROP%%file_path.file_name.extension
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplemented
        return True
        pass