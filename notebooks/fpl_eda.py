import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import altair as alt
    import orjson
    import polars as pl
    return alt, orjson, pl


@app.cell
def _(orjson):
    with open("data/2025-02-08T23:45:38.json", "rb") as f:
        data = orjson.loads(f.read())
    return data, f


@app.cell
def _(data, pl):
    teams = pl.DataFrame(data["teams"])
    return (teams,)


@app.cell
def _(teams):
    teams
    return


@app.cell
def _(alt, teams):
    alt.Chart(teams).mark_bar().encode(
        x="strength_attack_home",
        y=alt.Y("short_name").sort("-x"),
    )
    return


@app.cell
def _(alt, teams):
    alt.Chart(teams).mark_bar().encode(
        x="strength_attack_away",
        y=alt.Y("short_name").sort("-x"),
    )
    return


@app.cell
def _(alt, teams):
    alt.Chart(teams).mark_bar().encode(
        x="strength_defence_home",
        y=alt.Y("short_name").sort("-x"),
    )
    return


@app.cell
def _(alt, teams):
    alt.Chart(teams).mark_bar().encode(
        x="strength_defence_away",
        y=alt.Y("short_name").sort("-x"),
    )
    return


@app.cell
def _(data):
    data
    return


@app.cell
def _(pl):
    player_cols = {
        "element_type": pl.UInt8,
        "ep_next": pl.Float32,
        "ep_this": pl.Float32,
        "event_points": pl.Int8,
        "first_name": pl.String,
        "second_name": pl.String,
        "form": pl.Float32,
        "id": pl.UInt16,
        "points_per_game": pl.Float32,
        "selected_by_percent": pl.Float32,
        "team": pl.UInt8,
        "team_code": pl.UInt8,
        "total_points": pl.Int16,
        "transfers_in_event": pl.UInt32,
        "transfers_out_event": pl.UInt32,
        "now_cost": pl.Float32,
        "minutes": pl.UInt16,
        # Start here
        "goals_scored": pl.Float32,
        "assists": pl.Float32,
        "clean_sheets": pl.Float32,
        "goals_conceded": pl.Float32,
        "own_goals": pl.Float32,
        "penalties_saved": pl.Float32,
        "penalties_missed": pl.Float32,
        "yellow_cards": pl.Float32,
        "red_cards": pl.Float32,
        "saves": pl.Float32,
        "bonus": pl.Float32,
        "bps": pl.Float32,
        "influence": pl.Float32,
        "creativity": pl.Float32,
        "threat": pl.Float32,
        "ict_index": pl.Float32,
        "starts": pl.Float32,
        "expected_goals": pl.Float32,
        "expected_assists": pl.Float32,
        "expected_goal_involvements": pl.Float32,
        "expected_goals_conceded": pl.Float32,
        "expected_goals_per_90": pl.Float32,
        "saves_per_90": pl.Float32,
        "expected_assists_per_90": pl.Float32,
        "expected_goal_involvements_per_90": pl.Float32,
        "expected_goals_conceded_per_90": pl.Float32,
        "goals_conceded_per_90": pl.Float32,
    }
    return (player_cols,)


@app.cell
def _(data, pl, player_cols):
    pl.DataFrame(data["elements"]).select(player_cols.keys()).cast(player_cols)
    return


if __name__ == "__main__":
    app.run()
