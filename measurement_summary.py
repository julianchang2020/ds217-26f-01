# Replace this scaffold output with your calculation, loop, decision, and summary.
measurements = [18, 21, 24, 19]
review_threshold_text = "20"
review_threshold = int(review_threshold_text)
total = int(0)
review_count = int(0)

for measurement in measurements:
    total = total + measurement
    if measurement >= review_threshold:
        print("Measurement:", measurement, "review")
        review_count = review_count + 1
    elif measurement < review_threshold:
        print("Measurement:", measurement, "within range")
mean = sum(measurements)/len(measurements)
print("Count:", len(measurements))
print("Total:", total)
print("Mean:", mean)
print("Review count:", review_count)


