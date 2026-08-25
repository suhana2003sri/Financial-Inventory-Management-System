def calculate_gst(amount, gst_rate):
    gst = amount * gst_rate / 100
    total = amount + gst

    print("Amount:", amount)
    print("GST:", gst)
    print("Total Amount:", total)


calculate_gst(10000, 18)
