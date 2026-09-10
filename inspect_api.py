from agents import Agent, Runner, function_tool
import inspect

print("=== Agent.__init__ ===")
print(inspect.signature(Agent.__init__))

print("\n=== Runner.run ===")
print(inspect.signature(Runner.run))

print("\n=== function_tool ===")
print(inspect.signature(function_tool))

print("\n=== function_tool docstring ===")
print(function_tool.__doc__[:800] if function_tool.__doc__ else "No docstring")
