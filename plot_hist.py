import csv
import matplotlib.pyplot as plt

if __name__ == "__main__":
	platforms = ["gcp"]
	for idx, platform in enumerate(platforms):
		percentiles = [50, 66, 75, 80, 90, 95, 98, 99, 100, 0]
		csv_name = "logs_"+platform+"/log_500_distribution.csv"
		csv_file = open(csv_name)
		csv_reader = csv.reader(csv_file, delimiter=',')
		time = []
		time.append(0)
		for row in csv_reader:
			if "GET" in row[0]:
				for col in range(2,11):
					time.append(float(row[col]))
		print(time)
		plt.clf()
		# plt.hist(time,weights=percentiles) # A bar chart
		plt.xlabel('Time (in ms)')
		plt.ylabel('Percentile of requests')
		plt.ylim(0, 100)
		plt.xlim(0, time[-1])
		# for i in range(len(time)):
		# 	plt.hlines(bins=time[i],0,percentiles[i]) # Here you are drawing the horizontal lines
		data = time
		for i in range(len(data)):
			data[i] += 0.5
		plt.hist(data, bins=time, weights=percentiles, edgecolor='red')
		name = "Hist_"+platform+".png"
		plt.savefig(name)