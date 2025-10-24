import asyncio

from src.database import db


async def main():
    """Main function for analysis"""
    try:
        print("Connecting to the database...")

        sales_df = await db.get_all_sales()

        print(f"\n✅ Found {len(sales_df)} records in the 'sales' table")
        print("\n📊 DataFrame Information:")
        print(f"   - Shape: {sales_df.shape}")
        print(f"   - Columns: {list(sales_df.columns)}")

        if not sales_df.empty:
            print("\n📋 First 5 rows:")
            print(sales_df.head())

            print("\n📈 Descriptive statistics:")
            print(sales_df.describe())

        else:
            print("⚠️  The 'sales' table is empty or does not exist")

    except Exception as e:
        print(f"❌ Analysis error: {e}")

    finally:
        await db.close()


if __name__ == "__main__":
    asyncio.run(main())
