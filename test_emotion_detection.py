import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()