## Library Management System Comparison

### Code with Design Patterns:

# Singleton Pattern and Observer Pattern

# Classes: Book, LibrarySystem, Observer, User

# Pros:

# - Singleton pattern ensures only one instance of the LibrarySystem class exists.

# - Observer pattern allows users to receive notifications when books are added or removed.

# - Provides separation of concerns with the Observer pattern by decoupling the library system from the user-specific actions.

# Cons:

# - Introduces additional complexity with the implementation of design patterns.

# - May be overkill for a simple library management system.

### Code without Design Patterns:

# Class: Book, LibrarySystem

# Pros:

# - Simpler implementation without the need for additional classes or patterns.

# - Easier to understand and maintain for a basic library management system.

# Cons:

# - Lack of user-specific functionality such as borrowing and returning books.

# - No notification mechanism for users when books are added or removed.

# - Limited extensibility for adding new features or functionality.
