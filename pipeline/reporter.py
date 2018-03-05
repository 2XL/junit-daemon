import os


class ReportGenerator(object):
    def __init__(self, report_location='reports', report_extension_in='txt', report_extension_out='json'):
        self.report_location = report_location
        self.report_extension_in = report_extension_in

        pass

    def generate_json_report(self):
        print os.listdir(self.report_location)
        report_files = [pos_ for pos_ in os.listdir(self.report_location) if
                        pos_.endswith('.{}'.format(self.report_extension_in))]

        for report in report_files:
            parser = 'parse_{template}'.format(template=report.split('.')[0])
            if hasattr(self, parser):
                getattr(self, parser)()
        pass

    def parse_err_compile_source(self):
        raise NotImplementedError
        pass

    def parse_err_compile_test(self):
        raise NotImplementedError
        pass

    def parse_err_run_test(self):
        raise NotImplementedError
        pass

    def parse_out_compile_source(self):
        raise NotImplementedError
        pass

    def parse_out_compile_test(self):
        raise NotImplementedError
        pass

    def parse_out_run_test(self):
        raise NotImplementedError
        pass
