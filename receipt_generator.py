customer_name = input("Enter customer name: ")
num_tacos = int(input("Enter number of tacos: "))
price_per_taco = float(input("Enter price per taco: "))

#calculate the total
total_cost = num_tacos * price_per_taco

#format and display

print("\n--- Taco Receipt ---")
print("Customer: {}". format(customer_name))
print("Item: {:d} tacos @ ${:.2f} each" .format(num_tacos, price_per_taco))
print("Total: ${:.2f}" .format(total_cost))
print("Summary: {cnt} tacos at ${cost:.2f} each = ${sum:.2f}" .format(cnt=num_tacos, cost=price_per_taco, sum=total_cost))
print("Thanks for visiting {{Taco Town}}, {}!".format(customer_name))
