from bie import Pipeline, RunContext


class Stage:
    def __init__(self, name, artifact_key):
        self.name = name
        self.artifact_key = artifact_key

    def execute(self, ctx):
        ctx.artifacts[self.artifact_key] = True
        return ctx


class Gate:
    name = "artifact-present"

    def __init__(self, key):
        self.key = key

    def check(self, ctx):
        return bool(ctx.artifacts.get(self.key))


def test_pipeline_runs_stages_and_emits_completion():
    ctx = RunContext(run_id="test-1", source_uri="example.pdf")
    pipeline = Pipeline(
        stages=[Stage("ingestion", "ingested"), Stage("knowledge", "knowledge")],
        gates_by_stage={"ingestion": [Gate("ingested")]},
    )

    result = pipeline.run(ctx)

    assert result.errors == []
    assert result.artifacts["ingested"] is True
    assert result.artifacts["knowledge"] is True
    assert result.events[-1] == {"stage": "pipeline", "status": "COMPLETED"}


def test_pipeline_blocks_when_gate_fails():
    ctx = RunContext(run_id="test-2", source_uri="example.pdf")
    pipeline = Pipeline(
        stages=[Stage("ingestion", "ingested"), Stage("knowledge", "knowledge")],
        gates_by_stage={"ingestion": [Gate("missing")]},
    )

    result = pipeline.run(ctx)

    assert "knowledge" not in result.artifacts
    assert result.events[-1]["status"] == "BLOCKED"
