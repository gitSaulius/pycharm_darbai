
# class Blog:
#     def __init__(self):
#         self.posts = []
#     def create_post(self, pavadinimas, aprasymas):
#         post = {
#             "pavadinimas": pavadinimas,
#             "aprasymas": aprasymas
#         }
#
#         self.posts.append(post)
#         print("Irasas sekmingai sukurtas")
#
#     def display_all_posts(self):
#         if not self.posts:
#             print("No blog posts found")
#         else:
#             print("Blog posts: ")
#             for post in self.posts:
#                 print(f"pavadinimas: {post['pavadinimas']}")
#                 print(f"aprasymas: {post['aprasymas']}")
#                 print("--------")
#
#     def update_post(self, pavadinimas, naujas_aprasymas):
#         for post in self.posts:
#             if post["pavadinimas"] == pavadinimas:
#                post["aprasymas"] = naujas_aprasymas
#                print("Blog postas atnaujintas")
#                break
#         else:
#             print("Blog postas nerastas")
#
#     def delete_post(self, pavadinimas):
#         for post in self.posts:
#             if post["pavadinimas"] == pavadinimas:
#                 self.posts.remove(post)
#                 print("Irasas buvo sekmingai pasalintas")
#                 break
#         else:
#             print("Irasas nesurastas")
#
#
# post1 = Blog()
# post1.create_post("duomenu analitika uzkariauja pasauli", "analitika tampa svarbiausia BI dalis")
# post1.create_post("c", "analitika ir BI neatsiejami dalykai")
# post1.create_post("duomenu analitika toliau karaliauja BI srityje", "analitika, analitika ir dar karta analize")
# post1.update_post("duomenu analitika toliau karaliauja BI srityje", "analitika, analitika ir dar karta analitika")
# post1.delete_post("c")
# post1.display_all_posts()

# CRUD - create, read, update, delete


