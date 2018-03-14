# -*- coding: utf-8 -*-
# Copyright © 2017 Red Hat, Inc.
#
# This file is part of Bodhi.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""This module contains tests for bodhi.server.services.csrf.py"""
import unittest

import six

from bodhi.tests.server import base


class TestCSRFService(base.BaseTestCase):

    @unittest.skipIf(six.PY3, 'Not working with Python 3 yet')
    def test_csrf_html(self):
        """
        Assert that we return just the CSRF token when requesting HTML
        """
        res = self.app.get('/csrf', headers={'Accept': 'text/html'}, status=200)

        self.assertEquals(res.body, self.get_csrf_token())

    @unittest.skipIf(six.PY3, 'Not working with Python 3 yet')
    def test_csrf_json(self):
        """
        Assert that we return the CSRF token in JSON format when requesting JSON
        """
        res = self.app.get('/csrf', status=200)

        self.assertEquals(res.body, '{"csrf_token": "%s"}' % self.get_csrf_token())
