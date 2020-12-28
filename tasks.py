from invoke import task

@task(default=True)
def unit_test(ctx):
    ctx.run("py.test tests")

