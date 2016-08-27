defmodule Montecarlo do
  def main(args) do
    loops = 100_000_000
    c = 4
    result = run(loops, c)
    IO.puts result
  end
  def sample(_, 0, acc) do
    acc
  end

  def sample(state, n, acc) do
    {x, state} = :random.uniform_s(state)
    {y, state} = :random.uniform_s(state)

    res = x*x+y*y
    if res < 1 do
      sample(state, n-1, acc+1)
    else
      sample(state, n-1, acc)
    end
  end

  def sample(n, sender) do
    :random.seed(:erlang.now())
    result = sample(:random.seed(), n, 0)
    send sender, result
  end

  def run(samples, c) when is_integer(c) do
    n = trunc(samples / c)

    for _ <- 1..c do
      spawn(__MODULE__, :sample, [n, self])
    end

    results = for _ <- 1..c do
      receive do
        result -> result
      end
    end

    result = Enum.reduce(results, fn(acc, x) -> acc + x end)

    result / samples * 4
  end
end
