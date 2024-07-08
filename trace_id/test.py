import re
import unittest
from trace_id_creator import create_trace_id as create_trace_id


class TraceIdTest(unittest.TestCase):
    def test_create_uuid(self):
        result = create_trace_id()
        self.assertIsNotNone(result, "UUID V1이 생성 됐다면, 값이 Null이 아니다.")

        uuid_regex = r'^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
        self.assertIsNotNone(re.match(uuid_regex, result), "UUID V1이 생성 됐다면 UUID V1 양식을 만족한다.")
