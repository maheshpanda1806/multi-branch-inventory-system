# ShopSense Access Control Flow - Independent APIs

## Phase 1a: Owner Signup (User Creation)

```
POST /auth/signup
├─ Body: { email, password, username }
├─ Validation:
│  ├─ Email unique globally
│  ├─ Username unique globally
│  └─ Password meets requirements
├─ Create User
│  └─ is_staff=False (business owner, not platform admin)
│  └─ is_superuser=False
│  └─ is_active=True
└─ Return: { user_id, email, username }
```

---

## Phase 1b: Shop Creation

```
POST /api/shops
├─ Auth: User must be authenticated (is_active=True)
├─ Body: { name, address (optional) }
├─ Validation: Shop name required
├─ Create Shop
│  └─ owner = None initially (no auto-linking)
└─ Return: { shop_id, name, created_at }
```

---

## Phase 1c: Role Creation (Predefined Permission Sets)

```
POST /api/shops/{shop_id}/roles
├─ Auth: User must be shop owner (has ShopMembership with shop:own)
├─ Body: 
│  ├─ name (e.g., "Manager", "Cashier")
│  ├─ permission_set (enum: "manager" | "cashier" | "supervisor" | "custom")
│  ├─ custom_permissions[] (only if permission_set="custom")
│  └─ is_branch_scoped (bool: true for branch roles, false for shop-level)
├─ Validation:
│  ├─ Role name unique per shop
│  ├─ If permission_set in predefined → use those permissions
│  └─ If permission_set="custom" → use provided permissions
├─ Create Role
│  ├─ shop_id = target shop
│  ├─ is_branch_scoped = as provided
│  └─ permissions = selected permission objects
└─ Return: { role_id, name, is_branch_scoped, permissions[] }
```

---

## Phase 1d: Branch Creation

```
POST /api/shops/{shop_id}/branches
├─ Auth: User must be shop owner
├─ Body: { name, address (optional) }
├─ Validation: Branch name required per shop
├─ Create Branch
│  └─ shop_id = target shop
└─ Return: { branch_id, shop_id, name, address }
```

---

## Phase 2: Link Owner to Shop (Owner Membership)

```
POST /api/shops/{shop_id}/owner-membership
├─ Auth: Shop creator (user who created this shop)
├─ Body: { user_id (optional, defaults to current user) }
├─ Validation:
│  ├─ User exists
│  ├─ Shop exists
│  ├─ No existing membership for this user-shop pair
├─ Create Owner Role IF NOT EXISTS
│  └─ name = "Owner"
│  └─ is_branch_scoped = False
│  └─ permissions = [shop:own, ...]
├─ Create ShopMembership
│  ├─ user → shop → owner_role → branch=None
│  └─ is_active=True
└─ Return: { membership_id, user_email, shop_name, role_name }
```
---

## Phase 3: Bulk Employee Import (Branch Staffing)

```
POST /api/shops/{shop_id}/employees/bulk-import
├─ Auth: User must be shop owner
├─ Body: { employees[] }
│  └─ Each: { email, username, password, branch_id, role_name }
│
├─ VALIDATION PHASE
│  ├─ Validate row format
│  ├─ Validate email/username globally unique
│  ├─ Validate role_name exists in shop
│  ├─ Validate branch_id exists in shop
│  ├─ Validate role is branch-scoped
│  ├─ **Manager Uniqueness Check:**
│  │  ├─ Count existing active managers in this branch
│  │  ├─ Count proposed managers in CSV for this branch
│  │  └─ Reject if total > 1
│  └─ If all valid → proceed to creation
│
├─ CREATION PHASE (Transaction)
│  └─ For each validated row:
│     ├─ Create User (email, password, username)
│     ├─ Get Role object from shop
│     ├─ Create ShopMembership
│     │  ├─ user, shop, role, branch
│     │  └─ is_active=True
│     └─ Collect created records
│
└─ Return: { created_count, failed_count, errors[], created_users[] }
```

---

## Phase 4: Manager Replacement (Update Branch Manager)

```
PUT /api/shops/{shop_id}/branches/{branch_id}/manager
├─ Auth: User must be shop owner
├─ Body: { new_manager_email OR new_user_id }
├─ Get Current Manager Membership
├─ Deactivate old: is_active = False (audit trail)
├─ Create New ShopMembership (new_user → shop → manager_role → branch)
└─ Return: { old_manager_email, new_manager_email, timestamp }
```

---

## API Endpoint Summary

| Phase | Method | Endpoint | Purpose |
|-------|--------|----------|---------|
| 1a | POST | /auth/signup | Create user (signup) |
| 1b | POST | /api/shops | Create shop |
| 1c | POST | /api/shops/{id}/roles | Create role with permission set |
| 1d | POST | /api/shops/{id}/branches | Create branch |
| 2 | POST | /api/shops/{id}/owner-membership | Link owner to shop |
| 3 | POST | /api/shops/{id}/employees/bulk-import | Bulk create employees |
| 4 | PUT | /api/shops/{id}/branches/{bid}/manager | Replace branch manager |

---

## Example Flow (Step-by-Step)

```
1. POST /auth/signup
   → { user_id, email: owner@shop.com }

2. POST /api/shops
   → { shop_id, name: "MyShop" }

3. POST /api/shops/{id}/roles (Manager)
   → { role_id }

4. POST /api/shops/{id}/roles (Cashier)
   → { role_id }

5. POST /api/shops/{id}/branches
   → { branch_id, name: "Main Branch" }

6. POST /api/shops/{id}/owner-membership
   → { membership_id } (links owner to shop)

7. POST /api/shops/{id}/employees/bulk-import
   [
     { email: mgr@shop.com, branch_id, role_name: "Manager" },
     { email: cashier@shop.com, branch_id, role_name: "Cashier" }
   ]
   → Creates 2 users + 2 memberships

8. PUT /api/shops/{id}/branches/{bid}/manager
   → Replace manager with new_manager_email
```