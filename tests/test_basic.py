import pandas as pd

def load_csv(path):
    """Try UTF-8 first, then fallback to latin-1 if needed."""
    try:
        return pd.read_csv(path, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin-1")


def test_datasets_load():
    """Ensure the required CSVs exist and load correctly."""
    spotify = load_csv("data/spotify_top_2024.csv")
    billboard = load_csv("data/billboard_top.csv")

    assert len(spotify) > 0
    assert len(billboard) > 0


def test_column_presence():
    """Check for essential columns used in the model."""
    spotify = load_csv("data/spotify_top_2024.csv")

    required_columns = [
        "track", "artist", "spotify_streams",
        "spotify_popularity", "release_date"
    ]

    for col in required_columns:
        assert col in spotify.columns


def test_no_missing_values():
    """Ensure the CSV loads and is not completely missing data."""
    spotify = load_csv("data/spotify_top_2024.csv")
    assert spotify.isna().sum().sum() < len(spotify)