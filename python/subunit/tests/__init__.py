#
#  subunit: extensions to python unittest to get test results from subprocesses.
#  Copyright (C) 2005  Robert Collins <robertc@robertcollins.net>
#
#  Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
#  license at the users choice. A copy of both licenses are available in the
#  project source as Apache-2.0 and BSD. You may not use this file except in
#  compliance with one of these two licences.
#  
#  Unless required by applicable law or agreed to in writing, software
#  distributed under these licenses is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
#  license you chose for the specific language governing permissions and
#  limitations under that license.
#

from unittest import TestLoader

from subunit.tests import (
    test_chunked,
    test_details,
    test_progress_model,
    test_run,
    test_subunit_filter,
    test_subunit_stats,
    test_subunit_tags,
    test_tap2subunit,
    test_test_protocol,
    test_test_protocol2,
    test_test_results,
    )

def test_suite():
    loader = TestLoader()
    result = loader.loadTestsFromModule(test_chunked)
    result.addTest(loader.loadTestsFromModule(test_details))
    result.addTest(loader.loadTestsFromModule(test_progress_model))
    result.addTest(loader.loadTestsFromModule(test_test_results))
    result.addTest(loader.loadTestsFromModule(test_test_protocol))
    result.addTest(loader.loadTestsFromModule(test_test_protocol2))
    result.addTest(loader.loadTestsFromModule(test_tap2subunit))
    result.addTest(loader.loadTestsFromModule(test_subunit_filter))
    result.addTest(loader.loadTestsFromModule(test_subunit_tags))
    result.addTest(loader.loadTestsFromModule(test_subunit_stats))
    result.addTest(loader.loadTestsFromModule(test_run))
    return result
