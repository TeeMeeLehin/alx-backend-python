#!/usr/bin/env python3
"""testing the utils module"""
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """GithubOrgClient Test Class"""

    @parameterized.expand([('google',), ('abc',)])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """test func"""
        git_cli = GithubOrgClient(org_name)
        self.assertEqual(git_cli.org, {"payload": True})
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock, return_value={"repos_url": "norg.com"})
    def test_public_repos_url(self, mock_org):
        """test func"""
        git_cli = GithubOrgClient("norg")
        self.assertEqual(git_cli._public_repos_url, "norg.com")

