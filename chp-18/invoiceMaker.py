from prettytable import PrettyTable

def Main() :
    invoiceTable = PrettyTable()
    productTable = PrettyTable()
    calcTable = PrettyTable()
    invoice = {
        'products' : []
    }
    subtotal = 0
    print("===== Make Your Own Invoice =====\n")

    invoice['invoiceNo'] = int(input("Enter invoice number\n"))
    invoice['companyName'] = input("Enter company name\n")
    invoice['customerName'] = input("Enter customer name\n")
    invoice['mobile'] = input("Enter mobile number\n")
    invoice['address'] = input("Enter address\n")
    invoice['date'] = input("Enter date\n")

    productNo = int(input("Enter product number\n"))

    for i in range(productNo) :
        print("\n===== Fill Products Details =====\n")
        item = input("Enter item name\n")
        quantity = int(input("Enter quantity\n"))
        price = float(input("Enter price\n"))
        total = quantity * price

        subtotal = subtotal + total

        print("\n===== End Products Details =====\n")
        
        invoice['products'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'total': total
        })
    
    invoice['subtotal'] = subtotal
    invoice['tax'] = int(input("Enter tax percentage\n"))
    invoice['total'] = (subtotal + (subtotal * invoice['tax'] / 100))

    print("\n==== Your Invoice Details =====\n")
    
    invoiceTable.field_names = ['invoiceNo', 'companyName', 'customerName', 'mobile', 'address', 'date']
    invoiceTable.add_row([
        invoice['invoiceNo'],
        invoice['companyName'],
        invoice['customerName'],
        invoice['mobile'],
        invoice['address'],
        invoice['date']
    ]) 

    productTable.field_names = ['Item', 'Quantity', 'Price', 'Total']

    for product in invoice['products'] :
        productTable.add_row([
            product['item'],
            product['quantity'],
            product['price'],
            product['total']
        ])
    
    calcTable.field_names = ['Subtotal', 'Tax', 'Total']
    calcTable.add_row([
        invoice['subtotal'],
        invoice['tax'],
        invoice['total'],
    ])

    print("\n---- Invoice Table ---- \n")
    print(invoiceTable)
    print("\n---- Product Table ---- \n")
    print(productTable)
    print("\n---- Calc Table ---- \n")
    print(calcTable)

Main()