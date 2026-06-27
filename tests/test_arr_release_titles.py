# -*- coding: utf-8 -*-

import unittest

from quasarr.api.arr import _release_title_for_client


class ArrReleaseTitleTests(unittest.TestCase):
    def test_arr_clients_receive_parseable_release_title(self):
        title = "Sample.Show.2026.06.19.1080p.WEB.h264-GRP"

        for request_from in [
            "Sonarr/4.0.17.2952",
            "Radarr/6.1.1.10360",
            "Lidarr/2.0.0",
            "Magazarr/1.0.0",
        ]:
            with self.subTest(request_from=request_from):
                self.assertEqual(
                    title,
                    _release_title_for_client(title, "dl", request_from),
                )

    def test_unknown_clients_keep_hostname_badge(self):
        self.assertEqual(
            "[DL] Sample.Release",
            _release_title_for_client("Sample.Release", "dl", "Unknown/1.0"),
        )


if __name__ == "__main__":
    unittest.main()
