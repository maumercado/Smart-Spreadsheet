import unittest

if __name__ == "__main__":
  unittest.TextTestRunner().run(unittest.TestLoader().discover('tests', pattern='*.py'))
