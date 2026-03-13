queue = []

# Print jobs add karo (enqueue)
queue.append("Document1.pdf")
queue.append("Photo.jpg") 
queue.append("Report.docx")

print("Print Queue:", queue)

# Print karo (dequeue - FIFO)
print("Printing:", queue.pop(0))  # Document1.pdf first
print("Printing:", queue.pop(0))  # Photo.jpg next

print("Remaining:", queue)