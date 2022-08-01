import psycopg2
from dotenv import dotenv_values
import pandas as pd

config = dotenv_values(".env")


def get_data_from_reddit(filename):
    df = pd.read_csv(filename)
    df["type"] = "suicide"
    reddit_data = df[["title", "type"]]
    return reddit_data.head(5)


def get_data_from_twitter(filename):
    df = pd.read_csv(filename, sep='\t', lineterminator='\n')
    df = df.iloc[:, 1:]
    df["type"] = "suicide"
    df.columns = ["title", "type"]
    return df.head(5)


def prepare_data(reddit_data, twitter_data):
    df = pd.concat([reddit_data, twitter_data], names=[
                   'title', 'type'], ignore_index=True)
    print(df.head(10))
    return None


def insert_data(data):
    try:
        conn = psycopg2.connect(config["DBURI"], sslmode='require')
        cur = conn.cursor()
        for index, row in data.iterrows():
            cur.execute("insert into dataset values (%s, %s, %s)",
                        [index, row["title"], row['type']])
        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(e)
        cur.close()
        conn.close()

    return None


def reset_data():
    try:
        conn = psycopg2.connect(config["DBURI"], sslmode='require')
        cur = conn.cursor()
        cur.execute("DROP TABLE dataset;")
        cur.execute(
            "CREATE TABLE dataset (id serial PRIMARY KEY, description text, type varchar);")
        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(e)
        cur.close()
        conn.close()

    return None


if __name__ == "__main__":
    reddit_data = get_data_from_reddit("RedditData.csv")
    twitter_data = get_data_from_twitter("tweets.csv")
    data = prepare_data(reddit_data, twitter_data)
    # insert_data(data)
