#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64, json, os, sys, yaml

from invoke import task
from pipeline import executor, reporter, exporter


@task
def clean(ctx):
    """ Cleans up generated files, clean all files in source
    """
    # cleanup migration
    ctx.run('rm -rf src/*')
    ctx.run('rm -rf out/*')
    ctx.run('rm -rf tests/*')
    ctx.run('rm -rf reports/*')


@task
def report(ctx):
    """Generate json reports from execution stdout

    :param ctx:
    :return:
    """
    ctx.run('rm -rf reports/*.json')
    report_generator = reporter.ReportGenerator()
    report_generator.generate_report()
    report_generator.export_json_report()


@task
def export(ctx, source_home='src', test_home='tests', fixture_home='fixture', fixture_name='exported_challenge.yml', is_correct=False):
    """Generate fixture yml from src and tests

    :param ctx:
    :param source_home: (default:'src')
    :param test_home: (default:'tests')
    :param fixture_home: (default:'fixture')
    :param fixture_name: (default:'exported_challenge.yml')
    :param is_correct: (default:False)
    :return:

    """
    # need placeholder name which should be equal to the fixture content hash
    fixture_exporter = exporter.FixtureExporter(
        source_home=source_home,
        test_home=test_home,
        fixture_home=fixture_home,
        is_correct=is_correct,
        fixture_name=fixture_name)

    fixture_exporter.generate_fixture()
    fixture_exporter.export_yml_fixture()


@task(pre=[clean], post=[])
def build(ctx, code=None, language='java', fixture=None, test='junit', case='answer'):
    """Provision the project with the provided payload
         # -c   answer submitted by the user        - expect it to be k/v = relative path to `project`
         # -t   test framework                      `default: pytest` # dummy field
         # -f   assertion_fixture, code             - expect it to be k/v = relative path to `project`, json encoded
         # -l   java                                `default: java` # dummy field
    :param ctx:
    :param code:
    :param language:
    :param fixture:
    :param test:
    :param case:
    :return:
    """

    # if __name__ == "__main__":
    #     case = 'answer'
    #     code = None
    #     fixture = None

    data = None

    # provision submission with option: -f file_path.yml
    if fixture is not None:
        with open(fixture, 'r') as fixture_stream:
            challenge = yaml.load(fixture_stream)
            code_submission = '\n'.join(challenge['challenge'][case]['files'])
            valid_assertion = '\n'.join(challenge['challenge']['valid_assertion']['files'])
            data = '\n'.join([code_submission, valid_assertion])

    # provision submission from exported_challenge.json
    elif code is None:
        # load default bootstrap source for demo
        with open('data/exported_challenge.json', 'r') as file_stream:
            challenge = json.load(file_stream)
            code_submission = '\n'.join(challenge['challenge'][case]['files'])
            valid_assertion = '\n'.join(challenge['challenge']['valid_assertion']['files'])
            data = '\n'.join([code_submission, valid_assertion])
    else:
        # provision submission with option: -c "string with source code"
        data = code

    submission = executor.PipelineExecutor()
    submission.load_queue_from_submission(code=data)
    # submission.list_queue()
    submission.apply_queue()
    pass
