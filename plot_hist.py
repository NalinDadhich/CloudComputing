import csv
import matplotlib.pyplot as plt

if __name__ == "__main__":
	platforms = ["gcp", "aws", "azure"]
	for idx, platform in enumerate(platforms):
		percentiles = [50, 16, 9, 5, 10, 5, 3, 1, 1]
		csv_name = "logs_"+platform+"/log_500_distribution.csv"
		csv_file = open(csv_name)
		csv_reader = csv.reader(csv_file, delimiter=',')
		time = []
		for row in csv_reader:
			if "GET" in row[0]:
				for col in range(2,11):
					time.append(float(row[col]))
		print(time)
		plt.clf()
		plt.hist(time,weights=percentiles) # A bar chart
		plt.xlabel('Time')
		plt.ylabel('Percentile')
		plt.ylim(0, 50)
		for i in range(len(time)):
			plt.hlines(time[i],0,percentiles[i]) # Here you are drawing the horizontal lines
		name = "Hist_"+platform+".png"
		plt.savefig(name)