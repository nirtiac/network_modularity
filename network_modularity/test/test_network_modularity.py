import unittest
from .. import network_modularity
import os
from StringIO import StringIO

class NetworkModularityTest(unittest.TestCase):

    filepath = filepath = os.path.dirname(os.path.realpath(__file__)) + "/test_karate.ncol"
    
    def setUp(cls):
        parser = network_modularity.create_parser()
        cls.parser = parser
    
    def test_no_args(self):
        with self.assertRaises(SystemExit):
            args = self.parser.parse_args([])

    def test_bad_input(self):
        with self.assertRaises(SystemExit):
            args = self.parser.parse_args(["aaa.tsv"])
            out = StringIO()
            network_modularity.process_args(args, out)

    def test_infomap(self):
        args = self.parser.parse_args([self.filepath, "-i"])
        output = self.get_output(args)
        self.assertEquals("0.402038132807", output)
        
    def test_multilevel(self):
        args = self.parser.parse_args([self.filepath, "-m"])
        output = self.get_output(args)
        self.assertEquals("0.419789612097", output)

    def test_label_prop(self):
        args = self.parser.parse_args([self.filepath, "-m"])
        output = self.get_output(args)
        self.assertNotEquals("ERR", output) #because output can vary

    def test_output_communities_infomap(self):
        args = self.parser.parse_args([self.filepath, "-i", "-o"])
        output = self.get_output(args)
        self.assertIn("0,1", output)

    def test_directed_infomap(self):
        args = self.parser.parse_args([self.filepath, "-i", "-d"])
        output = self.get_output(args)
        self.assertEquals("0.0", output)

    def get_output(self, args):
        filepath = os.path.dirname(os.path.realpath(__file__)) + "/test_karate.ncol"
        out = StringIO()
        network_modularity.process_args(args, out)
        output = out.getvalue().strip()
        return output

if __name__ == "__main__":
    unittest.main()
