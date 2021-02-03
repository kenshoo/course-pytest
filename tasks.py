from invoke import task

@task(default=True)
def test(ctx, module=""):
    ctx.run(f"py.test tests/{module}.py")

