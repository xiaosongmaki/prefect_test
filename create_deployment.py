from prefect import flow
# Source for the code to deploy (here, a GitHub repo)
SOURCE_REPO="https://github.com/xiaosongmaki/prefect_test.git"

if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="test.py:show_stars", # Specific flow to run
    ).deploy(
        name="my-second-deployment",
        parameters={
            "github_repos": [
                "PrefectHQ/prefect",
                "pydantic/pydantic",
                "huggingface/transformers"
            ]
        },
        work_pool_name="my_mac",
        cron="*/1 * * * *",  # Run every 1 minute
    )