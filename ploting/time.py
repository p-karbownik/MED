import pandas as pd
import matplotlib.pyplot as plt


def create_time_chart(supports: list, time: list, title: str, plot_path: str, plot_format: str):
    plt.clf()
    plt.plot(supports, time)
    plt.title(title)
    plt.xlabel("Support")
    plt.ylabel("Execution time [ms]")

    plt.savefig(f"{plot_path}", format=plot_format)


def draw_time_charts():
    time_charts_names = ["cinema",
                         "ksiazki",
                         "movies",
                         "muzyka",
                         "politics"]

    for n in time_charts_names:
        df = pd.read_csv("./results/time/" + n + ".csv")
        df.round({'time': 0})
        create_time_chart(df['support'], df['time'], "Execution time for dataset " + n + ".csv", "./results/time"
                                                                                                 "/plots/" + n +
                          ".png", "PNG")

        if n != "muzyka":
            n_df = df.iloc[1:, :]

            create_time_chart(n_df['support'], n_df['time'], "Execution time for dataset " + n + ".csv", "./results/time"
                                                                                                     "/plots/" + n +
                              "2.png", "PNG")
            if n == "cinema":
                n_df = n_df.iloc[3:, :]

                create_time_chart(n_df['support'], n_df['time'], "Execution time for dataset " + n + ".csv",
                                  "./results/time"
                                  "/plots/" + n +
                                  "3.png", "PNG")
