# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from nose.tools import eq_, ok_

from configman import class_converter
from configman.dotdict import DotDict

from socorrolib.unittest.testbase import TestCase
from socorrolib.app.for_application_defaults import (
    ApplicationDefaultsProxy,
    ValueSource,
)
from socorrolib.app.socorro_app import App


#==============================================================================
# for use in a later test
class SomeApp(App):
    @classmethod
    def get_application_defaults(klass):
        defaults = DotDict()
        defaults.alpha = 17
        defaults.beta = 23
        return defaults


#==============================================================================
class TestApplicationDefaultsProxy(TestCase):

    def setUp(self):
        self.proxy = ApplicationDefaultsProxy()

    def test_app_converter(self):
        # temp shim, cannot load the socorro classes to test
        #eq_(
        #   self.proxy.str_to_application_class('collector'),
        #   class_converter('socorrolib.collector.collector_app.CollectorApp')
        #)
        #eq_(
        #   self.proxy.str_to_application_class('crashmover'),
        #   class_converter('socorrolib.collector.crashmover_app.CrashMoverApp')
        #)
        #eq_(
        #   self.proxy.str_to_application_class('submitter'),
        #   class_converter('socorrolib.collector.submitter_app.SubmitterApp')
        #)
        #eq_(
            #self.proxy.str_to_application_class('crontabber'),
            #class_converter('socorrolib.cron.crontabber_app.CronTabberApp')
        #)
        #eq_(
        #   self.proxy.str_to_application_class('middleware'),
        #  class_converter('socorrolib.middleware.middleware_app.MiddlewareApp')
        #)
        #eq_(
        #    self.proxy.str_to_application_class('processor'),
        #    class_converter('socorrolib.processor.processor_app.ProcessorApp')
        #)
        #eq_(
        #    self.proxy.str_to_application_class(
        #        'socorrolib.external.hb.hbase_client.HBaseClientApp'
        #    ),
        #  class_converter('socorrolib.external.hb.hbase_client.HBaseClientApp')
        #)
        pass

    def test_application_defaults(self):
        new_proxy = ApplicationDefaultsProxy()
        eq_(new_proxy.application_defaults, DotDict())

        new_proxy.str_to_application_class(
            'socorrolib.unittest.app.test_for_application_defaults.SomeApp'
        )

        eq_(
            dict(new_proxy.application_defaults),
            {
                'alpha': 17,
                'beta': 23,
            }
        )


#==============================================================================
class TestValueSource(TestCase):

    def test_get_values(self):
        new_proxy = ApplicationDefaultsProxy()
        vs = ValueSource(new_proxy)
        eq_(
            vs.get_values(None, None, dict),
            {}
        )
        eq_(
            vs.get_values(None, None, DotDict),
            DotDict()
        )
        new_proxy.str_to_application_class(
            'socorrolib.unittest.app.test_for_application_defaults.SomeApp'
        )
        eq_(
            vs.get_values(None, None, dict),
            {
                'alpha': 17,
                'beta': 23,
            }
        )
        ok_(isinstance(vs.get_values(None, None, DotDict), DotDict))
