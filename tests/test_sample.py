import generic as g


class SampleTest(g.unittest.TestCase):

    def test_sample(self):
        m = g.get_mesh('featuretype.STL')

        samples = m.sample(1000)

        # check to make sure all samples are on the mesh surface
        distance = m.nearest.signed_distance(samples)
        assert (g.np.abs(distance) < g.trimesh.tol.merge).all()

        even, index = g.trimesh.sample.sample_surface_even(m, 1000)
        # check to make sure all samples are on the mesh surface
        distance = m.nearest.signed_distance(even)
        assert (g.np.abs(distance) < g.trimesh.tol.merge).all()


if __name__ == '__main__':
    g.trimesh.util.attach_to_log()
    g.unittest.main()
