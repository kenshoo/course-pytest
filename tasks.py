from invoke import task

@task
def test(ctx, module=""):
    ctx.run(f"py.test tests/{module}.py")

@task
def tests(ctx):
    ctx.run(f"py.test tests")
