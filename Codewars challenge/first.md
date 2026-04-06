# 🧠 Python Lists — Revision Notes

## 1. What is a list?

A **list** is an ordered, changeable collection of items.

```python
numbers = [1, 2, 3, 4]
```

### Key properties:

- Ordered ✅ (has index)
- Mutable ✅ (can change)
- Can store multiple data types ✅

---

## 2. Indexing

```python
numbers = [10, 20, 30]

numbers[0]  # 10
numbers[1]  # 20
```

### Negative indexing:

```python
numbers[-1]  # last item → 30
```

---

## 3. Adding elements

### append() → add to end

```python
numbers.append(5)
```

### insert() → add at specific index

```python
numbers.insert(1, 99)
```

---

## 4. Removing elements

### remove() → by value

```python
numbers.remove(10)
```

### pop() → by index

```python
numbers.pop()    # last item
numbers.pop(0)   # first item
```

⚠️ Important:

- `remove(value)`
- `pop(index)`

---

## 5. Updating values

```python
numbers[0] = 100
```

---

## 6. Looping through a list

```python
for num in numbers:
    print(num)
```

---

## 7. Condition inside loop

```python
for num in numbers:
    if num > 20:
        print(num)
```

---

## 8. Check if item exists

```python
if 10 in numbers:
    print("Found")
```

---

## 9. Length of list

```python
len(numbers)
```

---

## 10. Sorting

```python
numbers.sort()
```

---

## 11. Slicing

```python
numbers = [1, 2, 3, 4, 5]

numbers[1:4]  # [2, 3, 4]
```

Format:

```
[start:end]
```

---

## 12. Important concept

👉 Lists are **mutable**

```python
numbers = [1, 2, 3]
numbers.append(4)
```

This changes the original list.

---

## 13. Common mistakes

❌ Using wrong method:

```python
numbers.pop(10)   # wrong if index doesn't exist
```

❌ Confusing value vs index:

- `remove(10)` → removes value
- `pop(1)` → removes index

❌ Poor variable naming:

```python
for user in numbers:  # confusing
```

✅ Better:

```python
for num in numbers:
```

---

## 14. Mental model (very important)

Think of a list as:

```
[ item0, item1, item2, item3 ]
   ↑       ↑       ↑
 index0  index1  index2
```

---

## 15. Real-world usage

Lists are used for:

- users
- products
- API responses
- database results

---

## 16. Your core toolkit (memorise this)

You should be comfortable with:

```python
append()
insert()
remove()
pop()
len()
for loop
if condition
indexing
slicing
```

---

## 17. Final tip (developer mindset)

Don’t just memorise methods.

Always ask:

> “Am I working with an index or a value?”

---
