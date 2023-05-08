import os
import requests
from github import Github

# First create a Github instance:

# using an access token
g = Github(os.environ["KYR_ACCESS_TOKEN"])

# # Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print(repo.name)

lorem_ipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum porta vel nibh in congue. Phasellus facilisis odio sit amet lectus ornare, non ultricies leo vestibulum. Mauris in diam at dolor euismod vehicula. Morbi ut nibh luctus, congue risus quis, blandit augue. Duis quis iaculis nisi, mattis aliquet lectus. Integer lacinia elementum libero. Fusce at erat a ex egestas dictum ut in risus. Vestibulum imperdiet, nulla vitae ultricies aliquam, ante elit maximus erat, sed tempor ipsum lorem nec sem.

Quisque porta arcu eget dui bibendum molestie. Vestibulum non massa feugiat arcu posuere eleifend vitae eget nisi. Sed at bibendum purus, sed auctor odio. Suspendisse tincidunt, sapien sit amet pulvinar rutrum, magna tellus pharetra purus, nec finibus tortor augue sed ex. Suspendisse egestas sit amet dolor in vestibulum. Ut eget lorem eget enim lobortis porttitor sed sed est. In malesuada scelerisque metus sit amet aliquam. Aenean elit sapien, tempor vitae malesuada ac, mattis sit amet eros. Cras ac nisi vel tellus rhoncus tristique. Aenean mattis vitae tortor in eleifend. Aenean finibus, justo ac commodo sollicitudin, augue odio hendrerit dolor, aliquet egestas dolor erat sed eros. Pellentesque tristique dui nec tortor pretium varius. Nam tincidunt est leo, auctor efficitur magna ultricies non.

Proin ac malesuada urna. Suspendisse vitae interdum turpis. In placerat mauris libero, et dapibus nisi ultrices vitae. Vestibulum malesuada odio ac placerat suscipit. Maecenas turpis enim, tristique nec varius in, pharetra a tortor. Suspendisse magna leo, elementum et venenatis nec, pellentesque iaculis leo. Etiam eget urna tristique, commodo est eget, semper velit. Nam id rutrum velit. Morbi imperdiet condimentum lacus eget consequat. Vivamus ultrices sem erat, id pretium ex laoreet vel. Praesent malesuada eu elit vel ultricies. Maecenas ullamcorper consectetur ante, sed feugiat elit bibendum non.

Maecenas viverra urna a bibendum lobortis. Integer ex quam, porta ac elit non, dignissim viverra risus. Sed tristique mauris eget accumsan euismod. Vivamus a tincidunt ipsum, in placerat dolor. Nulla malesuada mi nec nisi vehicula, id consectetur diam accumsan. Phasellus pharetra mauris eu odio pharetra porta. Praesent convallis orci et aliquam auctor. Maecenas rhoncus turpis sapien, vel auctor elit tempus ac. Donec tincidunt ligula in vehicula iaculis.

Proin tempor consequat posuere. Curabitur eget sapien pharetra, varius lacus id, tincidunt ante. Praesent nec ipsum in nulla malesuada pharetra ut vel lacus. Cras cursus lorem sed neque tempus, eu blandit purus egestas. In vitae orci et erat dictum suscipit. Proin orci ligula, ultricies ut aliquam sit amet, congue sed justo. Sed erat quam, sollicitudin quis turpis id, faucibus scelerisque est. Cras nec risus dapibus, condimentum augue sit amet, sollicitudin sapien. Fusce mollis leo est, sit amet iaculis mi rhoncus ac. Curabitur sodales aliquet mi eget suscipit. Aenean sodales ultricies diam, sed sodales ex convallis ac. Mauris id pulvinar magna. In hac habitasse platea dictumst.
"""

file_name = "README.md"
file = open(f'{file_name}', 'w')
file.write("#Algorithm Study Manager\n")
file.write(lorem_ipsum)
file.close()


