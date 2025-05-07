# GAP Python+AI Workshop

Sample project to use in our workshop.


Create the python virtual environment with the following commands:

```bash
    python3 -m venv venv
    source venv/bin/activate
```


## Setup

To run the app it's necessary to have several services installed and up and running.
Just run the following command:

```bash
    ./run/setup.sh
```

Run tests with:

```
pytest
```

Run the app with:

```
python app.py
```

## Workshop Instructions:

### 1. The project tree (unix command):

```
mkdir -p AI/context && tree -L 4 -I "AI|node_modules|docs|target|__pycache__|venv|run" > AI/context/tree.md
```

### 2. The project stack

```
You are a solutions architect with expertise in modern web technologies.

Read requirements.txt file and AI/context/tree.md file, and create AI/context/tech_stack.md for ga-python-ai-workshop project.

Output Format: Create a markdown document with clear justifications and setup instructions, that permits easy expansion (additions and updates).

Detail specifically:
1. Core Technologies
   - Backend technologies
   - Database choice (postgresql)
2. Development Tools
3. Deployment Requirements
4. Version Requirements

Constraints:
- Maximum 1 choice per category
- Focus on stable, well-documented options
- Exclude experimental features

Provide specific version numbers and compatibility requirements.
```

### 3. Python Guidelines

Note: You can create many guidelines or rules.
- UI/UX guidelines (accessibility, ...).
- Frontend guidelines (Maintainable, easy to read, ...).
- Backend guidelines (Clean code, SOLID, ...).
- Model generation guidelines.

```
You are a specialized Python+Fastapi development consultant who creates optimized development guidelines.
You understand modern Python development practices, architectural patterns, and the importance of providing complete context in code generation.

Your task is to create rules based on our project's tech stack and requirements.

Reference these core files:
- Tree (./AI/context/tree.md)
- Tech Stack (./AI/context/tech_stack.md)

The rules will be saved to AI/context/python.md.

Include the following sections:

- Context-Aware Code Generation
- Code Style and Structure
- Framework Best Practices
- Testing and Quality
- Security and Performance
- API Design
- Database and Data Access
- Examples (with an User class example with proper documentation)

Example of a section output:

### Code Style and Structure
- Follow PEP 8 style guide and clean code principles
- Structure code in logical modules following domain-driven design
- Implement proper separation of concerns (router, controllers, models, services)
- Use modern Python features (type hints, dataclasses, async/await) appropriately
- Maintain consistent code formatting using Ruff or similar tools
- Use proper package structure and __init__.py files
- Prefer short and pure functions.
- Prefer functional programming style if possible.
```


### 4. Unit Test Guidelines

```
You are a specialized Python+Pytest development consultant who creates optimized test guidelines.
You understand modern Python development practices, architectural patterns, and the importance of providing complete context in code generation.

Your task is to create rules based on our project's tech stack and requirements.
Write the rules one at a time, confirming with me.

Reference these core files:
- Tree (./AI/context/tree.md)
- Tech Stack (./AI/context/tech_stack.md)
- Python Rules (./AI/context/python.md)
- conftest setup (./src/tests/conftest.py)
- Factories setup (./src/tests/factories.py)
- Database setup (./src/services/orm.py)

Important Considerations:
- SQLAlchemy’s autoflush is enabled.
- Factories call automatically flush after object creation.
- No commit() calls in tests: Using commit() will persist data and may break test isolation.
- Test Isolation: Each test must be atomic and independent, without relying on prior test states.

The rules will be saved to AI/context/pytest.md.

Include:
- Best Practices for AI-Generated Tests
- Session Handling Rules
- Relationship Integrity
- Follow the “AAA” Pattern (Arrange-Act-Assert)
- Add unit test examples.

Unit test Example:

def test_insert_invalid_author_id(db_session: Session) -> None:
    """
    Test to validate the author_id foreign key constraint.
    """
    # Arrange & Act & Assert
    with pytest.raises(IntegrityError):
        # Using a non-existent author_id should raise an IntegrityError
        invalid_uuid = uuid.uuid4()
        article = ArticleFactory(author_id=invalid_uuid)
        db_session.add(article)
        db_session.flush()

Finally add this at the bottom:

- Write one test file at a time (step by step).
- Make sure the following check-list is valid:
  1. Test methods parameters are annotated.
  2. Test methods are documented.
```

### 5. Gen: Unit Tests

```
Generate pytest unit tests for the files in ./src/models/*.py and place them in ./tests/models/ directory.
Follow the guidelines in ./AI/context/ files, specially ./AI/context/pytest.md.

... run pytest and make sure the tests are green
```

### 6. Code Analysis (Bonus)

```
Analyze [FILE] using AI/prompts/analysis.md instructions.
```

### 7. Understanding Code (Bonus)

```
Follow instructions in AI/prompts/explain.md for [FILE]
```
