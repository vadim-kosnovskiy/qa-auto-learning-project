import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user_ = github_api.get_user("defunkt")

    assert user_["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")

    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")

    assert r["total_count"] == 54
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")

    assert r["total_count"] == 0, "Repository 'sergiibutenko_repo_non_exist' not found"


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")

    assert r["total_count"] != 0, "Repository with a single letter name not found"


@pytest.mark.api
def test_emoji_list_not_empty(github_api):
    emojis_list = github_api.get_emojis_list()

    assert len(emojis_list) != 0, "Emoji list is empty"
    assert "ukraine" in emojis_list, "Not found emoji 'ukraine'"


@pytest.mark.api
def test_count_branches(github_api):
    branch_list = github_api.get_branch_list()
    name_branches = [branch["name"] for branch in branch_list]

    assert len(branch_list) == 5, "Count branches not equal 5"
    assert "main" in name_branches, "Not found branch main"


@pytest.mark.api
def test_not_only_one_author_added_commits(github_api):
    commit_list = github_api.get_commit_list()
    count_authors = set([c["commit"]["author"]["name"] for c in commit_list])

    assert len(count_authors) != 1, "Оnly one author added commits"
