from os import system
import csv
system("cls")
#-------------------------*100-ballik_masala*-------------------------------------------------------------------------------------------------------------------------------------
# def findMedianSortedArrays(nums1, nums2):
#     if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
#     l, r = 0, len(nums1)
#     while l <= r:
#         p1 = (l + r) // 2
#         p2 = (len(nums1) + len(nums2) + 1) // 2 - p1
#         m1 = nums1[p1 - 1] if p1 else float('-inf')
#         m2 = nums1[p1] if p1 != len(nums1) else float('inf')
#         n1 = nums2[p2 - 1] if p2 else float('-inf')
#         n2 = nums2[p2] if p2 != len(nums2) else float('inf')
#         if m1 <= n2 and n1 <= m2:
#             return (max(m1, n1) + min(m2, n2)) / 2 if (len(nums1) + len(nums2)) % 2 == 0 else max(m1, n1)
#         elif m1 > n2:
#             r = p1 - 1
#         else:
#             l = p1 + 1
#     raise ValueError("No median found")

# nums1 = [1, 3]
# nums2 = [2]
# print(findMedianSortedArrays(nums1, nums2)) 
#------------------------------------1-Masala----------------------------------------------------------------------------------------------------------------------------------------------------------
# file_name = 'product_material.txt'

# with open(file_name, 'r') as file:
#     lines = file.readlines()

# filtered_products = []

# for line in lines:

#     parts = line.strip().split(',')
    

#     product_id = parts[0]
#     material = parts[2]
#     price_str = parts[3]
#     is_available = parts[4] == 'true'

#     price = float(price_str.replace('$', '').replace(',', ''))
    
#     if 500 < price < 1000 and is_available:
#         filtered_products.append((product_id, material))

# for product_id, material in filtered_products:
#     print(f'ID: {product_id}, Material: {material}')
#---------------------------------------Masala-2-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# def read_product_data(file_path):
#     products = []
#     with open(file_path, mode='r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             products.append({
#                 'id': row[0],
#                 'product_code': row[1],
#                 'material': row[2],
#                 'price': float(row[3].replace('$', '').replace(',', '')),
#                 'is_available': row[4] == 'true'
#             })
#     return products

# def filter_and_sort_products(products, material_name):
#     filtered_products = [p for p in products if p['material'].lower() == material_name.lower() and p['is_available']]
#     sorted_products = sorted(filtered_products, key=lambda x: x['price'])
#     return sorted_products

# def display_products(products):
#     if products:
#         print(f"Products with material '{products[0]['material']}':")
#         for p in products:
#             print(f"ID: {p['id']}, Code: {p['product_code']}, Price: ${p['price']:.2f}")
#     else:
#         print("No available products found for the given material.")

# if __name__ == "__main__":
#     file_path = 'product_material.txt'
#     products = read_product_data(file_path)
    
#     material_name = input("Enter the material name: ")
#     filtered_sorted_products = filter_and_sort_products(products, material_name)
    
#     display_products(filtered_sorted_products)
#----------------------------------Masala-3-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# file_name = 'product_material.txt'

# with open(file_name, 'r') as file:
    
#     for line in file:
#         parts = line.strip().split(',')


#         product_id = parts[0]
#         product_code = parts[1]
#         material = parts[2]
#         price = float(parts[3].replace('$', '').replace(',', ''))
#         is_available = parts[4] == 'true'
        
#         if price < 1000 and not is_available:
#             print(material)




