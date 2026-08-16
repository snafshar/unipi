import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]

def load(folder, filename):
    path = ROOT / folder / filename
    spec = importlib.util.spec_from_file_location(folder, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class AlgorithmTests(unittest.TestCase):
    def test_logistic_regression_learns_and(self):
        m = load('logistic-regression', 'logistic_regression.py')
        w, b = m.fit([[0,0],[0,1],[1,0],[1,1]], [0,0,0,1])
        predictions = [int(m.sigmoid(sum(a*c for a,c in zip(w, row))+b) >= .5)
                       for row in [[0,0],[0,1],[1,0],[1,1]]]
        self.assertEqual(predictions, [0,0,0,1])

    def test_kmeans_separates_clusters(self):
        m = load('kmeans', 'kmeans.py')
        centroids, groups = m.kmeans([[1,1],[1,2],[8,8],[9,8]])
        self.assertEqual([len(group) for group in groups], [2,2])
        self.assertEqual(centroids, [[1.0,1.5],[8.5,8.0]])

    def test_naive_bayes_classifies_known_word(self):
        m = load('naive-bayes', 'naive_bayes.py')
        predict = m.train(['good film','bad film'], ['pos','neg'])
        self.assertEqual(predict('good'), 'pos')

if __name__ == '__main__':
    unittest.main()
