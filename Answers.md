    Q1.
    A class is a blueprint that defines attributes and methods,
    whlie an object is an instance of a class.
    Example: **Book** is a class, and a specific book like 
    "Database System" is an object.

     Q2
     Encapsulation means hiding data and controlling access
    through methods.
    In the **Loan** class, loan details like due data and return date should be private and modified using methods.

    Q3
    -Association: A simple relationship between classes.
    Example: Member borrows Loan.
    -Aggregation: A weak whole-part relationship.
    Example: Library has Books.
    -Composition: A strong whole-part relationship.
    Example: Loan contains Loan details that cannot exist without the loan.

    Q4
    Inheritance allows one class to reuse properties and methods of another class.
    Example: A **Person** class can be created as a parent class for **Member** and **Librarian** because both have common attributes like name and email.

    Q5
    Polymorphism allows the same method to have different behaviors depending on the object.
    Example: A method 'displayinfo()' can work differently for Member and Librarian.

    Q6
    A use case diagram shows system functions and interactions with actors.
    A sequence diagram shows the order of messages exchanged between objects during an operation.

    Q7
    'include' means a use case always uses another use case.
    Example: Borrow Book includes Login.
    'extend' adds optional behavior.
    Example: Late Return extends Return Book.

    Q8
    A state machine diagram shows the different states of an object and transition between them.
    It helps understand chhanges better than a simple text description.

    Q9
    Multiplicity shows how many objects can be related.
    In the diagram: One Member can have many Loans (1..*), while each Loan belongs to one another(1).

    Q10
    Object-oriented approach uses classes and objects that combine data and behavior.
    Procedural programming focuses on functions and step-by-step instruction without organizing data as objects.

    Q11
    Imperative explains how to do atask step by step, while Declarative explains what result is needed.

    Q12
    A pure function gives the same output for the same output for the same input and avoids changing external data.
    This reduces errors.

    Q13
    OOP organizes code into objects, making if easier to add features, reuse code, and maintain the program.

    Q14
    -Imperative: C
    -Object-oriented: Java
    -Functional: Haskell
    -Declarative: SQL

    Q15
    Python supports multiple paradigms:
    imperative, object-oriented, and functional pragramming.

    Q16
    Functional programming is useful for data processing and calculations because it gives predictable results.

    Q17
    UML designs object-oriented systems, while OOP implements the design using classes and objects.

    Q18
    Django uses object-oriented and declarative programming Models use classes, and QuerySet describe data request.