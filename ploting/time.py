import pandas as pd
import matplotlib.pyplot as plt


def create_time_chart(supports_stage1: list, time_stage1: list, supports_stage2: list, time_stage2: list, title: str,
                      plot_path: str,
                      plot_format: str):
    plt.clf()
    plt.plot(supports_stage1, time_stage1, label="noBitArray")
    plt.plot(supports_stage2, time_stage2, label="bitArray")
    plt.title(title)
    plt.legend()
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
        df_stage1 = pd.read_csv("./results/time/" + n + ".csv")
        df_stage1.round({'time': 0})

        df_stage2 = pd.read_csv("./results/time_stage2/" + n + ".csv")
        df_stage2.round({'time': 0})

        create_time_chart(df_stage1['support'], df_stage1['time'], df_stage2['support'], df_stage2['time'],
                          "Execution time for dataset " + n + ".csv", "./results/time"
                                                                      "/plots/" + n +
                          ".png", "PNG")

        if n != "muzyka":
            n_df = df_stage1.iloc[1:, :]
            n_df2 = df_stage2.iloc[1:, :]
            create_time_chart(n_df['support'], n_df['time'], n_df2['support'], n_df2['time'],
                              "Execution time for dataset " + n + ".csv",
                              "./results/time"
                              "/plots/" + n +
                              "2.png", "PNG")
            if n == "movies":
                n_df = n_df.iloc[2:, :]
                n_df2 = n_df2.iloc[2:, :]

                create_time_chart(n_df['support'], n_df['time'], n_df2['support'], n_df2['time'],
                                  "Execution time for dataset " + n + ".csv",
                                  "./results/time"
                                  "/plots/" + n +
                                  "3.png", "PNG")
            if n == "cinema":
                n_df = n_df.iloc[3:, :]
                n_df2 = n_df2.iloc[3:, :]

                create_time_chart(n_df['support'], n_df['time'], n_df2['support'], n_df2['time'],
                                  "Execution time for dataset " + n + ".csv",
                                  "./results/time"
                                  "/plots/" + n +
                                  "3.png", "PNG")
