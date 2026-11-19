import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AirQualityAnalyzer:

    def __init__(self):
        self.data = None
        self.graph = None


    def load_data(self):
        try:
            print("Load Dataset")
            self.data = input("Enter the path of the csv file: ")
            self.data = pd.read_csv(f"{self.data}")
            print("Dataset loaded successfully! ")
            return self.data
        except:
            print("Please enter valid path")


    def explore_data(self):
        try:
            if self.data is None:
                print("Please Load the Dataset First!")
                return
            print("Select an option: ")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display the column names")
            print("4. Display data types")
            print("5. Display basic info ")
            print("6. Convert Date column (text to date)")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print(self.data.head())
            elif choice == 2:
                print(self.data.tail())
            elif choice == 3:
                print(self.data.columns)
            elif choice == 4:
                print(self.data.dtypes)
            elif choice == 5:
                self.data.info()
            elif choice == 6:
                self.convert_date()
            else:
                print("Invalid Input")

        except:
            print("Something went wrong!!")

    def convert_date(self):
        try:
            self.data["Date"] = pd.to_datetime(self.data["Date"], format="%d/%m/%Y").dt.date
            print("Date column converted to date successfully!")
        except:
            print("Something went wrong!")


    def dataframe_op(self):
        try:
            if self.data is None:
                print("Please Load the Dataset First !")
                return
            print("=== DataFrame Operations ===")
            print("1. Average Temperature")
            print("2. Top 5 Hottest Readings")
            print("3. Top 5 Coldest Readings")
            print("4. Date with Highest Average CO")
            print("5. Top 5 Dates with Highest Average NO2")

            choice = int(input("Enter Your Choice :-"))

            if choice == 1:
                print(self.data['T'].mean())

            elif choice == 2:
                print(self.data.nlargest(5, "T")[["Date", "Time", "T"]])

            elif choice == 3:
                print(self.data.nsmallest(5, "T")[["Date", "Time", "T"]])

            elif choice == 4:
                print(self.data.groupby("Date")["CO(GT)"].mean().nlargest(1))

            elif choice == 5:
                print(self.data.groupby("Date")["NO2(GT)"].mean().nlargest(5))

            else:
                print("Enter a valid Choice !")

        except:
            print("Something went wrong!")


    def filter_data(self):
        try:
            if self.data is None:
                print("Please Load the Dataset First!")
                return

            print("Select an option:")
            print("1. Display rows With Missing Values ")
            print("2. Fill missing Values with 0")
            print("3. Drop rows with Missing Values")
            print("4. Replace Missing Values with a Specific Value ")

            choice = int(input("Enter your Choice : "))

            if choice == 1:
                missing = self.data.isnull()
                total = int(missing.sum().sum())
                if total == 0:
                    print("No Missing Values Found in the Dataset !")
                else:
                    print(f"Total missing values: {total}")
                    print("\nMissing values per column:")
                    print(missing.sum()[missing.sum() > 0])
                    print("\nRows with missing values:")
                    print(self.data[missing.any(axis=1)])

            elif choice == 2:
                self.data = self.data.fillna(0)
                print("Missing values filled with 0 successfully!")
                print(self.data.isnull().sum())

            elif choice == 3:
                print("=== Before Cleaning ===")
                print(self.data.isnull().sum())
                self.data = self.data.dropna().reset_index(drop=True)
                print("=== After Cleaning ===")
                print(self.data.isnull().sum())
                print(f"Rows remaining: {len(self.data)}")

            elif choice == 4:
                replace = input("Enter a Value to Replace it with Missing Value : ")
                try:
                    replace = float(replace)     
                except:
                    pass                        
                self.data = self.data.fillna(replace)
                print(f"Missing Values Replaced with {replace} Successfully ! ")

            else:
                print("Invalid Choice !!")

        except:
            print("Something went wrong!")


    def statistics_data(self):
        try:
            if self.data is None:
                print("Please Load the Dataset First!")
                return

            num = self.data[["CO(GT)", "C6H6(GT)", "NOx(GT)", "NO2(GT)", "T", "RH", "AH"]]

            print("=== Descriptive Statistics ===")
            print("1. Display Summary Statistics")
            print("2. Display Mean of Numeric Columns")
            print("3. Display Median of Numeric Columns")
            print("4. Display Minimum and Maximum Values")
            print("5. Display Standard Deviation")
            print("6. Display Variance")

            choice = int(input("Enter  Your Choice :- "))

            if choice == 1:
                print(self.data.describe())
            elif choice == 2:
                print(num.mean())
            elif choice == 3:
                print(num.median())
            elif choice == 4:
                print("MINIMUM :\n", num.min())
                print("MAXIMUM :\n", num.max())
            elif choice == 5:
                print(num.std())
            elif choice == 6:
                print(num.var())
            else:
                print("Enter a valid Choice !")

        except:
            print("Something went wrong!")


    def data_visualization(self):
        try:
            if self.data is None:
                print("Please Load the Dataset First!")
                return
            print()
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart ")
            print("5. Histogram ")
            choice = int(input("Enter your Choice : "))

            if choice == 1:
                column = input("Enter column to group by (e.g. Date): ")
                value = input("Enter numeric column for Y-axis (e.g. NO2(GT)): ")

                data = self.data.groupby(column)[value].mean().nlargest(10)
                data.plot(kind="bar")
                plt.title(f"{value} by {column}")
                plt.xlabel(column)
                plt.ylabel(value)
                plt.xticks(rotation=45)
                plt.legend()
                self.graph = plt.gcf()
                plt.show()

            elif choice == 2:
                x = input("Enter X-axis column (e.g. Date): ")
                y = input("Enter Y-axis column (e.g. T): ")

                data = self.data.groupby(x)[y].mean()
                data.plot(kind="line")
                plt.title(f"{y} by {x}")
                plt.xlabel(x)
                plt.ylabel(y)
                plt.xticks(rotation=45)
                plt.legend()
                self.graph = plt.gcf()
                plt.show()

            elif choice == 3:
                x = input("Enter X-axis column (e.g. T): ")
                y = input("Enter Y-axis column (e.g. RH): ")

                self.data.plot(kind="scatter", x=x, y=y, label=f"{y} vs {x}")
                plt.title(f"{y} vs {x}")
                plt.xlabel(x)
                plt.ylabel(y)
                plt.legend()
                self.graph = plt.gcf()
                plt.show()

            elif choice == 4:
                column = input("Enter category column (e.g. Date): ")
                value = input("Enter numeric column (e.g. CO(GT)): ")

                data = self.data.groupby(column)[value].mean().nlargest(10)
                data.plot(kind="pie", autopct="%1.1f%%")
                plt.title(f"{value} by {column}")
                plt.ylabel("")
                plt.legend(bbox_to_anchor=(1, 1))
                self.graph = plt.gcf()
                plt.show()

            elif choice == 5:
                column = input("Enter numeric column (e.g. T): ")

                self.data[column].plot(kind="hist", bins=10)
                plt.title(f"Distribution of {column}")
                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.legend()
                self.graph = plt.gcf()
                plt.show()

            else:
                print("Enter a valid Choice !")

        except:
            print("Something went wrong !")

    def save_visualization(self):
        try:
            if self.graph is None:
                print("No chart to save. Create a chart first (option 6).")
                return

            filename = input("Enter file name (e.g. chart.png): ")
            if not filename.lower().endswith(".png"):
                filename += ".png"

            self.graph.savefig(filename, bbox_inches="tight")
            print(f"Visualization saved as {filename}")
        except:
            print("Something went wrong!")


    def main_menu(self):
        while True:
            print()
            print("========== Air Quality Analysis and Visualization Program ==========")
            print("Select an option: ")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform Dataframe Operations")
            print("4. Handle Missing Dataset")
            print("5. Generate Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Save Visualization")
            print("8. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except:
                print("Please enter a number!")
                continue

            if choice == 1:
                self.load_data()
            elif choice == 2:
                self.explore_data()
            elif choice == 3:
                self.dataframe_op()
            elif choice == 4:
                self.filter_data()
            elif choice == 5:
                self.statistics_data()
            elif choice == 6:
                self.data_visualization()
            elif choice == 7:
                self.save_visualization()
            elif choice == 8:
                print("Thank You for using Air Quality Analyzer! ")
                break
            else:
                print("Invalid Choice!")


if __name__ == "__main__":
    obj = AirQualityAnalyzer()
    obj.main_menu()