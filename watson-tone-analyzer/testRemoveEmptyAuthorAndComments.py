
import unittest

from removeEmptyAuthorAndCommenty import removeEmptyAuthor, removeEmptyBody


class TestremoveEmptyAuthorAndBody(unittest.TestCase):

    def testremoveEmptyAuthor(self):
        comments = [{
            "author": "Scott Frederick",
            "body": "Spring Boot 2.4 is compatible with Kotlin 1.4. Spring Boot 2.5 [will support]( Kotlin 1.5. We'll pick up the upgrade from Kotlin  to  as part of our semi-automated dependency upgrade process before the Boot 2.5.0 release. ",
            "id": 26371
        },
            {
            "author": None,
            "body": "Strictly speaking, I think we require 1.3.x or later as our Kotlin code is [compiled with a 1.3 API and language version]( The default Kotlin version provided by dependency management then changes across Boot 2.3, 2.4, and 2.5.",
            "id": 26371
        }]

        expect_comments = [{
            "author": "Scott Frederick",
            "body": "Spring Boot 2.4 is compatible with Kotlin 1.4. Spring Boot 2.5 [will support]( Kotlin 1.5. We'll pick up the upgrade from Kotlin  to  as part of our semi-automated dependency upgrade process before the Boot 2.5.0 release. ",
            "id": 26371
        },]

        removeEmptyAuthor(comments)
        self.assertEquals(len(expect_comments), len((comments)))
        self.assertListEqual(expect_comments,comments)

    def testremoveEmptyBody(self):
        comments = [{
            "author": "Scott Frederick",
            "body": "Spring Boot 2.4 is compatible with Kotlin 1.4. Spring Boot 2.5 [will support]( Kotlin 1.5. We'll pick up the upgrade from Kotlin  to  as part of our semi-automated dependency upgrade process before the Boot 2.5.0 release. ",
            "id": 26371
        },
            {
            "author": "Scott Frederick",
            "body": "",
            "id": 26371
        }]

        expect_comments = [{
            "author": "Scott Frederick",
            "body": "Spring Boot 2.4 is compatible with Kotlin 1.4. Spring Boot 2.5 [will support]( Kotlin 1.5. We'll pick up the upgrade from Kotlin  to  as part of our semi-automated dependency upgrade process before the Boot 2.5.0 release. ",
            "id": 26371
        }   ]

        removeEmptyBody(comments)
        self.assertEquals(len(expect_comments), len((comments)))
        self.assertListEqual(expect_comments,comments)

    def testremoveEmptyAuthorAndBody(self):
        comments = [{
            "author": "Scott Frederick",
            "body": "Spring Boot 2.4 is compatible with Kotlin 1.4. Spring Boot 2.5 [will support]( Kotlin 1.5. We'll pick up the upgrade from Kotlin  to  as part of our semi-automated dependency upgrade process before the Boot 2.5.0 release. ",
            "id": 26371
        },
            {
            "author": "Scott Frederick",
            "body": "",
            "id": 26371
        },
         {
            "author": None,
            "body": "Strictly speaking, I think we require 1.3.x or later as our Kotlin code is [compiled with a 1.3 API and language version]( The default Kotlin version provided by dependency management then changes across Boot 2.3, 2.4, and 2.5.",
            "id": 26371
        }]

        expect_comments = [{
            "author": "Scott Frederick",
            "body": "Spring Boot 2.4 is compatible with Kotlin 1.4. Spring Boot 2.5 [will support]( Kotlin 1.5. We'll pick up the upgrade from Kotlin  to  as part of our semi-automated dependency upgrade process before the Boot 2.5.0 release. ",
            "id": 26371
        }   ]

        removeEmptyBody(comments)
        removeEmptyAuthor(comments)

        self.assertListEqual(expect_comments,comments)

if __name__ == '__main__':
    unittest.main()
