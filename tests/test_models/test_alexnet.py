import equinox as eqx
import jax

import eqxvision.models as models


class TestAlexNet:
    random_image = jax.random.uniform(key=jax.random.PRNGKey(0), shape=(1, 3, 224, 224))
    answer = (1, 1000)

    def test_output_shape(self, getkey):
        @eqx.filter_jit
        def forward(model, x, key):
            keys = jax.random.split(key, x.shape[0])
            return jax.vmap(model)(x, key=keys)

        model = models.alexnet(num_classes=1000)
        output = forward(model, self.random_image, getkey())
        assert output.shape == self.answer
