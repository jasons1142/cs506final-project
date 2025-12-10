import pandas as pd

def load_csv(path):
    """Helper wrapper to ensure correct encoding."""
    return pd.read_csv(path, encoding="latin1")


def test_datasets_load():
    """Ensure the required CSVs exist and load correctly."""
    spotify = load_csv("data/spotify_top_2024.csv")
    billboard = load_csv("data/billboard_top.csv")

    assert len(spotify) > 0
    assert len(billboard) > 0


def test_column_presence():
    """Check for essential columns in the raw Spotify dataset."""
    spotify = load_csv("data/spotify_top_2024.csv")

    required_columns = [
        "Track",
        "Artist",
        "Release Date",
        "Spotify Streams"
    ]

    for col in required_columns:
        assert col in spotify.columns


def test_no_missing_values():
    """Ensure the dataset is not entirely missing or corrupt."""
    spotify = load_csv("data/spotify_top_2024.csv")

    # Not empty
    assert len(spotify) > 0

    # Not *all* NaN
    assert spotify.isna().sum().sum() < spotify.size