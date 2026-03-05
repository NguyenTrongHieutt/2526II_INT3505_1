const express = require("express");
const router = express.Router();
const pool = require("../db");

// CREATE TABLE nếu chưa có
pool.query(`
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);
`);

// =============================
// Utility: Validate ID
// =============================
const isValidId = (id) => {
  return Number.isInteger(Number(id)) && Number(id) > 0;
};

// =============================
// GET - Lấy tất cả users
// =============================
router.get("/", async (req, res) => {
  try {
    const result = await pool.query("SELECT * FROM users ORDER BY id ASC");
    return res.status(200).json(result.rows);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: "Internal Server Error" });
  }
});

// =============================
// GET - Lấy user theo ID
// =============================
router.get("/:id", async (req, res) => {
  try {
    const { id } = req.params;

    if (!isValidId(id)) {
      return res.status(400).json({ message: "Invalid user ID" });
    }

    const result = await pool.query("SELECT * FROM users WHERE id = $1", [id]);

    if (result.rows.length === 0) {
      return res.status(404).json({ message: "User not found" });
    }

    return res.status(200).json(result.rows[0]);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: "Internal Server Error" });
  }
});

// =============================
// POST - Tạo user mới
// =============================
router.post("/", async (req, res) => {
  try {
    const { name, email } = req.body;

    // Validate dữ liệu
    if (!name || !email) {
      return res.status(400).json({
        message: "Name and email are required",
      });
    }

    // Check email trùng
    const emailCheck = await pool.query(
      "SELECT * FROM users WHERE email = $1",
      [email],
    );

    if (emailCheck.rows.length > 0) {
      return res.status(409).json({
        message: "Email already exists",
      });
    }

    const result = await pool.query(
      "INSERT INTO users(name, email) VALUES($1, $2) RETURNING *",
      [name, email],
    );

    return res.status(201).json(result.rows[0]);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: "Internal Server Error" });
  }
});

// =============================
// PUT - Update toàn bộ user
// =============================
router.put("/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const { name, email } = req.body;

    if (!isValidId(id)) {
      return res.status(400).json({ message: "Invalid user ID" });
    }

    if (!name || !email) {
      return res.status(400).json({
        message: "Name and email are required",
      });
    }

    // Kiểm tra user tồn tại
    const userCheck = await pool.query("SELECT * FROM users WHERE id = $1", [
      id,
    ]);

    if (userCheck.rows.length === 0) {
      return res.status(404).json({ message: "User not found" });
    }

    // Kiểm tra email trùng (trừ chính nó)
    const emailCheck = await pool.query(
      "SELECT * FROM users WHERE email = $1 AND id != $2",
      [email, id],
    );

    if (emailCheck.rows.length > 0) {
      return res.status(409).json({
        message: "Email already exists",
      });
    }

    const result = await pool.query(
      "UPDATE users SET name=$1, email=$2 WHERE id=$3 RETURNING *",
      [name, email, id],
    );

    return res.status(200).json(result.rows[0]);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: "Internal Server Error" });
  }
});

// =============================
// PATCH - Update một phần
// =============================
router.patch("/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const updates = req.body;

    if (!isValidId(id)) {
      return res.status(400).json({ message: "Invalid user ID" });
    }

    if (Object.keys(updates).length === 0) {
      return res.status(400).json({
        message: "No fields provided for update",
      });
    }

    // Kiểm tra user tồn tại
    const userCheck = await pool.query("SELECT * FROM users WHERE id = $1", [
      id,
    ]);

    if (userCheck.rows.length === 0) {
      return res.status(404).json({ message: "User not found" });
    }

    // Build dynamic query
    const fields = [];
    const values = [];
    let index = 1;

    for (let key in updates) {
      fields.push(`${key} = $${index}`);
      values.push(updates[key]);
      index++;
    }

    values.push(id);

    const result = await pool.query(
      `UPDATE users SET ${fields.join(", ")} WHERE id = $${index} RETURNING *`,
      values,
    );

    return res.status(200).json(result.rows[0]);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: "Internal Server Error" });
  }
});

// =============================
// DELETE - Xóa user
// =============================
router.delete("/:id", async (req, res) => {
  try {
    const { id } = req.params;

    if (!isValidId(id)) {
      return res.status(400).json({ message: "Invalid user ID" });
    }

    const result = await pool.query(
      "DELETE FROM users WHERE id = $1 RETURNING *",
      [id],
    );

    if (result.rowCount === 0) {
      return res.status(404).json({ message: "User not found" });
    }

    return res.status(204).send();
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: "Internal Server Error" });
  }
});

module.exports = router;
