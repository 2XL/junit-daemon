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
        raise NotImplementedError
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
        #raise NotImplementedError
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
        #raise NotImplementedError
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
        #raise NotImplementedError
        pass
