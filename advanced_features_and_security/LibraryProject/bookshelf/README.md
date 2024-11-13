The Post model defines the following permissions:

- can_view : Allows viewing posts.
- can_create: Allows creating new post.
- can_edit: Allows editing posts.
- can_delete: Allows deleting posts.

Each view that requires specific permissions uses the @permission_required decorator:

- post_list: Requires can_view
- create_post: Requires can_create
- edit_post: Requires can_edit
- delete_post: Requires can_delete
