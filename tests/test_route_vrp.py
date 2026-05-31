import unittest

from src.kpi import KPIWeights, normalize_weights
from src.route_vrp import optimize_route


class RouteOptimisationTests(unittest.TestCase):
    def test_zero_weights_fall_back_to_equal_normalized_weights(self):
        weights = normalize_weights(KPIWeights(0, 0, 0, 0))
        self.assertEqual(weights, KPIWeights(0.25, 0.25, 0.25, 0.25))

    def test_isolated_kpis_can_change_the_recommended_route(self):
        cases = {
            "distance": KPIWeights(1, 0, 0, 0),
            "time": KPIWeights(0, 1, 0, 0),
            "co2": KPIWeights(0, 0, 1, 0),
            "congestion": KPIWeights(0, 0, 0, 1),
        }
        results = {
            name: optimize_route(use_mock=True, weights=weights)
            for name, weights in cases.items()
        }

        routes = {tuple(route) for route, _ in results.values()}
        self.assertGreater(
            len(routes),
            1,
            "Changing KPI priorities should affect at least one recommended route.",
        )

        metric_rows = {
            tuple(metrics.values())
            for _, metrics in results.values()
        }
        self.assertGreater(
            len(metric_rows),
            1,
            "Changing KPI priorities should affect at least one displayed metric.",
        )


if __name__ == "__main__":
    unittest.main()
