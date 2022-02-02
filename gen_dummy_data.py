import random as rng
import string


def _gen_string(N):
	return "".join(rng.choices(string.ascii_lowercase, k=N))


def gen_dummy_data(N):
	cr_data = []
	up_data = []

	for i in range(N):
		cr_data.append({
			"stringvar": _gen_string(10),
			"numbervar": rng.randrange(1, 10000),
		})

		up_data.append({
			"stringvar": _gen_string(10),
			"numbervar": rng.randrange(1, 10000),
		})

	return (cr_data, up_data)
