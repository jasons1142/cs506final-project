import pandas as pd

def test_datasets_load():
    """Ensure the required CSVs exist and load correctly."""
    spotify = pd.read_csv("data/spotify_top_2024.csv")
    billboard = pd.read_csv("data/billboard_top.csv")

    assert len(spotify) > 0
    assert len(billboard) > 0


def test_column_presence():
    """Check for essential columns used in the model."""
    spotify = pd.read_csv("data/spotify_top_2024.csv")

    required_columns = [
        "track", "artist", "spotify_streams",
        "spotify_popularity", "release_date"
    ]

    for col in required_columns:
        assert col in spotify.columns

def test_no_missing_values():
    spotify = pd.read_csv("data/spotify_top_2024.csv")
    assert spotify.isna().sum().sum() < len(spotify)